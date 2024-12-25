nextflow.enable.dsl=2

process ALIGN {

    label 'high'
    tag 'Preprocessing'
    
    input: 
        tuple val(meta), path(reads)

    output:
        tuple val(meta), path('*Log.final.out')   , emit: log_final
        tuple val(meta), path('*Log.out')         , emit: log_out
        tuple val(meta), path('*Log.progress.out'), emit: log_progress

        tuple val(meta), path('*d.out.bam'), optional:true, emit: bam
        tuple val(meta), path("${prefix}.sortedByCoord.out.bam"), optional:true, emit: bam_sorted
        tuple val(meta), path("${prefix}.Aligned.sortedByCoord.out.bam") , optional:true, emit: bam_sorted_aligned
        tuple val(meta), path('*toTranscriptome.out.bam'), optional:true, emit: bam_transcript
        tuple val(meta), path('*Aligned.unsort.out.bam'), optional:true, emit: bam_unsorted
        tuple val(meta), path('*fastq.gz'), optional:true, emit: fastq
        tuple val(meta), path('*.tab'), optional:true, emit: tab
        tuple val(meta), path('*.SJ.out.tab'), optional:true, emit: spl_junc_tab
        tuple val(meta), path('*.ReadsPerGene.out.tab'), optional:true, emit: read_per_gene_tab
        tuple val(meta), path('*.out.junction'), optional:true, emit: junction
        tuple val(meta), path('*.out.sam'), optional:true, emit: sam
        tuple val(meta), path('*.wig'), optional:true, emit: wig
        tuple val(meta), path('*.bg'), optional:true, emit: bedgraph
}