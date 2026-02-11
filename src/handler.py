from strands_workflow import FuelOptimizationStrand
import json

def lambda_handler(event=None, context=None):
    strand = FuelOptimizationStrand()
    report = strand.run()

    with open("output/sample_report.json", "w") as f:
        json.dump(report, f, indent=2)

    return {
        "statusCode": 200,
        "body": report
    }

if __name__ == "__main__":
    lambda_handler()
