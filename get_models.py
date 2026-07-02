from pathlib import Path

root = Path("/neelin2020/CMIP6-HISTORICAL/")

models = []

for model_dir in root.iterdir():
    if not model_dir.is_dir():
        continue

    pr_dir = model_dir / "pr"
    if not pr_dir.is_dir():
        continue

    # Check whether any .nc file contains "3hr" in its filename
    #if any("3hr" in f.name for f in pr_dir.glob("*.nc")):
    if any("3hr" in f.name and "2014" in f.name  for f in pr_dir.glob("*.nc")):
        models.append(model_dir.name)

print(models)
print(len(models))

'''
['IPSL-CM6A-LR', 'KACE-1-0-G', 'CNRM-CM6-1-HR', 'CMCC-CM2-ESM2', 'HadGEM3-GC31-LL', 'MRI-ESM2-0', 'MPI-ESM1-2-LR', 'FGOALS-g3', 'IITM-ESM', 'MIROC-ES2L', 'CMCC-CM2-SR5', 'GISS-E2-1-G', 'BCC-CSM2-MR', 'SAM0-UNICON', 'CNRM-CM6-1', 'GISS-E2-1-G_otherData', 'IPSL-CM5A2-INCA', 'IPSL-CM6A-LR-INCA', 'CNRM-ESM2-1', 'NESM3', 'HadGEM3-GC31-MM', 'GFDL-CM4', 'ACCESS-ESM1-5', 'UKESM1-0-LL', 'ACCESS-CM2', 'AWI-ESM-1-1-LR', 'MPI-ESM1-2-HR', 'CanESM5', 'TaiESM1']
'''