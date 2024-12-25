nextflow.enable.dsl=2

process FASTP {

    label 'standard'
    tag 'Preprocessing'

    input: 
        tuple val(meta), path(reads)
 
    output:
        tuple val(meta), path("${meta.id}/fastp/*.trimmed_*.fastq.gz"), emit: trimmed_reads
        // Trimming report
        path "${meta.id}/fastp/*.json", emit: json
        path "${meta.id}/fastp/*.html", emit: html
        // path '${sample_id}/fastp/*.log', emit: log
        path "${meta.id}/fastp/*.failed.fastq.gz", optional: true, emit: failed_out
        path "${meta.id}/fastp/*.unpaired_*.fastq.gz", optional: true, emit: unpaired_reads

    script:
        def input_args = reads.size() == 1 ? "-i ${reads[0]}" : "-i ${reads[0]} -I ${reads[1]}"
        def out_args = reads.size() == 1 ? "-o ${meta.id}/fastp/${meta.id}.trimmed_r1.fastq.gz" 
                : "-o ${meta.id}/fastp/${meta.id}.trimmed_r1.fastq.gz -O ${meta.id}/fastp/${meta.id}.trimmed_r2.fastq.gz"
        def failed_args = meta.save_failed_trim ? ( 
            reads.size() == 1 ?
                "--failed_out ${meta.id}/fastp/${meta.id}.failed.fastq.gz" 
                : "--failed_out ${meta.id}/fastp/${meta.id}.failed.fastq.gz \
                    --unpaired1 ${meta.id}/fastp/${meta.id}.unpaired_r1.fastq.gz \
                    --unpaired2 ${meta.id}/fastp/${meta.id}.unpaired_r2.fastq.gz"
        ) : ""
        def output_dir = new File("${meta.id}/fastp")
        if (!output_dir.exists()) {
            output_dir.mkdirs()
        }
        """
            # mkdir -p ${meta.id}/fastp
            
            fastp \\
                ${task.ext.args} \\
                -w ${task.cpus} \\
                ${input_args} \\
                ${out_args} \\
                -j ${meta.id}/fastp/${meta.id}.json \\
                -h ${meta.id}/fastp/${meta.id}.html \\
                ${failed_args}
        """
}