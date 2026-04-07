"""
EA-Openclaw Insurance Quote Request
Comprehensive Motor Vehicle Insurance - Quote Submission
"""

import json
from datetime import date


def build_quote_request():
    quote = {
        "quote_type": "comprehensive_motor",
        "submission_date": date.today().isoformat(),

        "policy_holder": {
            "full_name": "Nilesh Cooray",
            "licence_cancellations": False,
            "traffic_infringements": False,
        },

        "vehicle": {
            "registration": "DIU-471",
            "make": "Tesla",
            "garage_location": {
                "unit": "G1",
                "street": "354 Tooronga Rd",
                "suburb": "Glen Iris",
                "state": "VIC",
                "country": "AU",
            },
        },

        "cover": {
            "type": "Comprehensive",
            "includes": [
                "Accidental damage",
                "Theft and attempted theft",
                "Fire damage",
                "Storm and hail damage",
                "Third party property damage",
                "Emergency repairs",
                "Towing costs",
                "EV battery and charging equipment",
            ],
        },

        "claims_history": {
            "at_fault_accidents": 0,
            "not_at_fault_accidents": 0,
            "theft_claims": 0,
            "other_claims": 0,
        },

        "rating_factors": {
            "no_claim_bonus_eligible": True,
            "clean_driving_record": True,
            "garaged_overnight": True,
        },
    }
    return quote


def main():
    request = build_quote_request()
    print("=== EA-Openclaw Comprehensive Insurance Quote Request ===\n")
    print(json.dumps(request, indent=2))
    print("\nQuote request built successfully.")
    print("Policy holder : Nilesh Cooray")
    print("Vehicle       : Tesla  |  Rego: DIU-471")
    print("Garage        : G1, 354 Tooronga Rd, Glen Iris VIC")
    print("Cover type    : Comprehensive")
    print("Driving record: Clean — no accidents, claims, cancellations or fines")
    return request


if __name__ == "__main__":
    main()
