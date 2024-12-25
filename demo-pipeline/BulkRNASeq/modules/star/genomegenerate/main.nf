nextflow.enable.dsl=2

process GenomeGenerate {

    label 'high'
    tag 'Preprocessing'
    
    input:
        tuple val(meta), path(trimmed_reads)
        path fasta
        path gtf
    
    output:
        tuple val(meta), path(trimmed_reads)
        path("${meta.id}/genome"), emit: sample_idx
    
    script:
        // Set two-pass options.
        def sjdb_args = meta.sjdb ? "--sjdbFileChrStartEnd ${meta.sjdb}" : ""
        def memory      = task.memory ? "--limitGenomeGenerateRAM ${task.memory.toBytes() - 100000000}" : ''
        
        // make genome path
        def genome_dir = new File("${meta.id}/genome")
        if (!genome_dir.exists()) {
            genome_dir.mkdirs()
        }
        """
            STAR \\
                --runMode genomeGenerate \\
                --genomeDir ${genome_dir} \\
                --genomeFastaFiles $fasta \\
                --sjdbGTFfile $gtf \\
                --runThreadN $task.cpus \\
                $memory \\
                ${task.ext.args}
        """
}