This project implements a Proof-of-Concept (POC) Airline Fuel Optimization Agent designed to:

* Ingest flight plan data
* Apply simplified weather influence
* Estimate fuel consumption
* Recommend optimal cruise altitude

The workflow is structured in modular execution stages following a stateful orchestration pattern aligned with AWS workflow principles. It is designed for deployment using AWS Lambda and operational messaging via Amazon SNS or Amazon SQS.

---

# Architecture

Flight Data (CSV)
 ↓
Ingestion
↓
Weather Simulation
↓
Fuel Estimation
 ↓
Altitude Optimization
 ↓
MCP Recommendation Output

Each stage operates on a shared state object, modeling a Strands-style stateful execution flow.

---

# Implemented Features

Flight Data Ingestion:

* Reads flight information from CSV
* Includes:

  * Origin
  * Destination
  * Planned altitude
  * Distance
  * Aircraft type


->Simplified Weather Model (Non-Segmented)

Weather is modeled as a single aggregated factor affecting the entire flight

There is:

* No route segmentation
* No waypoint-based weather

->Random Weather Generation

Weather is simulated using controlled random values:

{
  "headwind_knots": random.choice([-20, -10, 0, 10, 20]),
  "turbulence": random.choice(["none", "light", "moderate"]),
  "temp_deviation_c": random.choice([-5, 0, 5])
}

This allows:

* Testing wind impact on fuel burn
* Simulating operational variability
* Evaluating optimization response to different conditions

->Weather Assumption:

A single average enroute wind component affects total cruise fuel burn.
This is a simplification suitable for POC purposes.

->Fuel Estimation Logic

Fuel burn is calculated using:

Fuel = Distance × BaseBurnRate


Then adjusted for:

* Headwind / tailwind factor
* Altitude efficiency difference
* Turbulence penalty

This produces a total estimated cruise fuel value.


->Altitude Optimization

The optimizer evaluates:

* Planned altitude
* Planned −2000 ft
* Planned +2000 ft

Each scenario recalculates fuel burn and selects the minimum fuel option.

Output includes:

* Original fuel burn
* Optimized fuel burn
* Estimated fuel savings
* Recommended cruise altitude


->AWS Alignment

Designed for execution in:

* AWS Lambda
* Orchestrated via AWS Step Functions for production-scale workflow control
* Input/output stored in Amazon S3


# How to Run


python3 src/handler.py


Output:

* Console recommendation message
* JSON report file generated


# Limitations

* No enroute waypoint modeling
* No altitude-layer wind modeling
* No real METAR/TAF integration
* No airway or ATC constraints
* No payload or weight modeling
* Simplified aircraft performance curve



# Future Improvements

* Implement route segmentation
* Integrate real cruise wind (e.g., 250 hPa layer)
* Add cost index modeling (fuel vs time)
* Add emissions impact calculation
