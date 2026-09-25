import os
import unittest
import yaml

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestBosajProfile(unittest.TestCase):
    def test_community_standards_exist(self):
        expected_files = ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md"]
        for f in expected_files:
            p = os.path.join(repo_root, f)
            self.assertTrue(os.path.exists(p), f"{f} should exist")
            self.assertGreater(os.path.getsize(p), 0)

    def test_github_workflows_valid_yaml(self):
        wf_dir = os.path.join(repo_root, ".github", "workflows")
        self.assertTrue(os.path.isdir(wf_dir))
        for yml_file in os.listdir(wf_dir):
            if yml_file.endswith((".yml", ".yaml")):
                full_path = os.path.join(wf_dir, yml_file)
                with open(full_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                self.assertIsInstance(data, dict, f"{yml_file} should parse to a valid dictionary")
                self.assertIn("name", data, f"{yml_file} should have a workflow name")


if __name__ == "__main__":
    unittest.main()
