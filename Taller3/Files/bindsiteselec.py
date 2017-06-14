import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import subprocess

name=sys.argv[1]
copy_name=name[:-4] + '_copy.pdb'
copy_file = open(copy_name, "w")
subprocess.call(['sed', 's/X/X /', name], stdout=copy_file)

site=np.genfromtxt(copy_name, skip_header=1, skip_footer=1)
res=site[:,5].astype(int)

ndx= np.sort(np.unique(res))
N=len(ndx)
texto=''
end=' | '
for i in range(N):
    if i==(N-1):
        end=''
    if not (ndx[i]-1 in ndx) and (ndx[i]+1 in ndx):
        texto = texto + ' r ' + str(ndx[i])
    elif (ndx[i]-1 in ndx) and (not (ndx[i]+1 in ndx)):
        texto = texto + '-' + str(ndx[i]) + end
    elif not (ndx[i]-1 in ndx) and not (ndx[i]+1 in ndx):
        texto= texto + ' r ' + str(ndx[i]) + end

print texto

os.remove(copy_name)
