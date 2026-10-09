import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from monster import decide, envelope, within

class GateTests(unittest.TestCase):
    def base(self):
        return {"preregistration":{"registered_before_outcomes":True,"protocol_id":"p1"},"metric":{"direction":"higher_is_better","tolerance":0.7},"baseline":{"matched":True},"conditions":[{"registered":True,"status":"complete","candidate":0.8,"baseline":0.75}],"failure_boundaries":[{"status":"not_observed_within_tested_range"}]}
    def test_pass_with_all_registered_conditions_inside_gate(self): self.assertEqual(decide(self.base()),"PASS")
    def test_first_bad_cell_fails(self):
        r=self.base(); r["conditions"].append({"registered":True,"status":"complete","candidate":0.69,"baseline":0.75})
        self.assertEqual(decide(r),"FAIL")
    def test_missing_registered_cell_is_na(self):
        r=self.base(); r["conditions"][0]["status"]="missing"
        self.assertEqual(decide(r),"N/A")
    def test_unmatched_baseline_is_na(self):
        r=self.base(); r["baseline"]["matched"]=False
        self.assertEqual(decide(r),"N/A")
    def test_failure_boundary_fails(self):
        r=self.base(); r["failure_boundaries"][0]["status"]="failure_observed"
        self.assertEqual(decide(r),"FAIL")
    def test_envelope_reports_extremes_and_mean(self): self.assertEqual(envelope([0.2,0.8]),{"worst":0.2,"best":0.8,"mean":0.5})
    def test_directions(self):
        self.assertTrue(within(0.8,"higher_is_better",0.7)); self.assertTrue(within(0.1,"lower_is_better",0.2)); self.assertTrue(within(0.5,"target_range",[0.4,0.6]))

if __name__=="__main__": unittest.main()
