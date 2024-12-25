// Bulk RNA-seq pipelines.

nextflow.enable.dsl=2

include { ExtractInfoFromFastq } from '../modules/utils'
// include { FASTP } from '../modules/fastp'

workflow LPWGS {
    // Define default fastq informations
    ch_fastq = Channel
        .fromFilePairs(params.input_dir + '/*R{1,2}*.fastq.gz')
        .map {
            meta, fastq ->
            def fmeta = [:]
            // Set meta.id
            fmeta.id = meta
            // Set meta.single_end
            if (fastq.size() == 1) {
                fmeta.single_end = true
            } else {
                fmeta.single_end = false
            }
            [ fmeta, fastq ]
        }
    // ch_fastq.view()
    
    // Update Fastq channel's meta informations
    ch_fastq = ch_fastq 
        | ExtractInfoFromFastq
        | map { meta, reads, v -> 
            def (flowcell_id, read_len) = v.trim().split("\t")
            // println "Flowcell ID: ${flowcell_id}, Read length: ${read_len}"
            
            meta.flowcell_id = flowcell_id
            meta.read_len = read_len
            meta.save_failed_trim = params.save_failed_trim
            meta.ref_ver = params.ref_ver
            [ meta, reads ]
        }
    // fastq_meta.view()

    ch_fastq.view()

    // trimmed_reads = input_channel.mix(save_failed_channel)
    //     | FASTP



    // View the output for testing
    // trimmed_reads.view()
}