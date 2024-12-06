// Bulk RNA-seq pipelines.

// mode = 'star'

// define process

// Trimming
process trim {
    input:
    path ''
    
    output: 
    path ''

    script: 
    """
    """
}

// define alignment methods
process star {
    input:
    path ''
    
    output: 
    path ''

    script: 
    """
    """

}

process salmon {
    input:
    path ''
    
    output: 
    path ''

    script: 
    """
    """

}

process htseq2 {
    input:
    path ''
    
    output: 
    path ''

    script: 
    """
    """
    
}

// run alignment by mode
process align {
    input:
    path ''
    
    output: 
    path ''

    script: 
    """
    """

}



// set workflow
workflow {
}

