
from pathlib import Path

_HERE = Path(__file__).parent; del Path

mt0 = _HERE / "mt/mt0.nii.gz"
mt1 = _HERE / "mt/mt1.nii.gz"
t1w = _HERE / "mt/t1w.nii.gz"
t2 = _HERE / "t2/t2.nii.gz"
t1 = _HERE / "t1/t1.nii.gz"
dmri = _HERE / "dmri/dmri.nii.gz"
bvals = _HERE / "dmri/bvals.txt"
bvecs = _HERE / "dmri/bvecs.txt"
fmri_crop_moco_mean_seg_manual = _HERE / "fmri/fmri_crop_moco_mean_seg_manual.nii.gz"
fmri = _HERE / "fmri/fmri.nii.gz"
t2s = _HERE / "t2s/t2s.nii.gz"
