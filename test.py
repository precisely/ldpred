"""
A test file for LDpred.
"""

import tempfile
import os

tf = tempfile.NamedTemporaryFile()
tmp_file_prefix = next(tempfile._get_candidate_names())

print 'Testing LDpred.\n'
print 'Note that this test currently only tests the core functionality of LDpred.'
print 'Please report bugs on gihub (https://github.com/bvilhjal/ldpred) or to Bjarni J Vilhjalmsson (bjarni.vilhjalmsson@gmail.com).\n'

coord_file = tmp_file_prefix + '.coord.hdf5'
print '\n\n\n\n\nCoordinating test data into file %s' % coord_file
cmd_str = 'python ./ldpred/coord_genotypes.py --gf=./test_data/LDpred_data_p0.001_train_0 --vgf=./test_data/LDpred_data_p0.001_test_0 --ssf=./test_data/LDpred_data_p0.001_ss_0.txt --N=10000  --out=%s' % coord_file
print cmd_str + '\n'
assert os.system(cmd_str) == 0, 'Problems when coordinating data!  Testing stopped'

print '\n\n\n\n\nCoordinating test data with LD file and results file prefix: %s ' % tmp_file_prefix
cmd_str = 'python ./ldpred/LDpred.py --coord=%s  --ld_radius=100   --local_ld_file_prefix=%s  --PS=0.001 --N=10000  --out=%s' % (coord_file, tmp_file_prefix, tmp_file_prefix)
print cmd_str + '\n'
assert os.system(cmd_str) == 0, 'Problems when running LDpred!  Testing stopped'

# tmp_file_prefix_pt = tmp_file_prefix + "-pt"
# print 'Running LD_pruning_thres, output file prefix: %s ' % tmp_file_prefix_pt
# cmd_str = 'python ./ldpred/LD_pruning_thres.py --coord=%s  --ld_radius=100  --out=%s' % (coord_file, tmp_file_prefix_pt)
# print cmd_str + '\n'
# assert os.system(cmd_str) == 0, 'Problems when running LD_pruning_thres!  Testing stopped'

out_file_prefix = tmp_file_prefix + '-res'
print '\n\n\n\n\nValidating results with output file prefix: %s' % tmp_file_prefix
cmd_str = 'python ./ldpred/validate.py --vgf=./test_data/LDpred_data_p0.001_test_0  --rf=%s  --out=%s' % (tmp_file_prefix, out_file_prefix)
print cmd_str + '\n'
assert os.system(cmd_str) == 0, 'Problems with the validation step!  Testing stopped'

# print 'Cleaning up files.'
# cmd_str = 'rm %s*' % tmp_file_prefix
# print cmd_str + '\n'
# assert os.system(cmd_str) == 0, 'Problems cleaning up test files!  Testing stopped'

print 'Test finished successfully!'
