# wig2rle -- a quick (somewhat misnamed) R script to convert a **bigwig** (not wig) file (e.g. from DANPOS
#            dpos via UCSC's wigToBigWig to a more-efficient Bioconductor RleList)
#  arguments: 1) path to INPUT file with bigwig
#             2) path to desired OUTPUT for the .RDS file containing the RleList object
# - 29 October 2018, Eric Zheng


# for my sanity - map some function names that I think exist to what actually exist
nrows <- nrow
ncols <- ncol
len <- length


library(rtracklayer)

args = commandArgs(trailingOnly=TRUE)
print(paste ("wig2rle: importing", args[1]) )

signals <- import.bw(args[1], as="RleList")

print(paste ("wig2rle: saving to", args[2]) )
saveRDS(signals, file = args[2])
