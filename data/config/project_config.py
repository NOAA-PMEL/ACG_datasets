import os
import json

platforms = {
    "VICKERS": {
        "name": "Vickers",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "SURVEYOR": {
        "name": "Surveyor",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "DISCOVERER": {
        "name": "Discoverer",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "RHBROWN": {
        "name": "RHBrown",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "KNORR": {
        "name": "Knorr",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "ATLANTIS": {
        "name": "Atlantis",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "REVELLE": {
        "name": "Revelle",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },
    "VODYANITSKIY": {
        "name": "Vodyanitskiy",
        "description": "",
        "url": "",
        "inlet_height": 18.0
    },

}
project_config = {
    "ATOMIC": {
        "project": "ATOMIC",
        "project_description": "Say something about atomic",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55-60%",
        # "trajectory_id": "ATOMIC_RHBrown"
    },
    "NAAMES4": {
        "project": "NAAMES-4",
        "project_description": "Say something about NAAMES-4",
        "project_url": "",
        "platform": platforms["ATLANTIS"]["name"],
        "target_sample_rh": "25-35%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "NAAMES3": {
        "project": "NAAMES-3",
        "project_description": "Say something about NAAMES-3",
        "project_url": "",
        "platform": platforms["ATLANTIS"]["name"],
        "target_sample_rh": "25-35%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "NAAMES2": {
        "project": "NAAMES-2",
        "project_description": "Say something about NAAMES-2",
        "project_url": "",
        "platform": platforms["ATLANTIS"]["name"],
        "target_sample_rh": "45-55%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
     "NAAMES1": {
        "project": "NAAMES-1",
        "project_description": "Say something about NAAMES-1",
        "project_url": "",
        "platform": platforms["ATLANTIS"]["name"],
        "target_sample_rh": "before 18-Nov: 20-50%, after 18-Nov: 55-65%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "WACS2014": {
        "project": "WACS-2",
        "project_description": "Say something about WACS-2",
        "project_url": "",
        "platform": platforms["KNORR"]["name"],
        "target_sample_rh": "47-55%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "WACS2012": {
        "project": "WACS",
        "project_description": "Say something about WACS",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55-65%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "DYNAMO": {
        "project": "DYNAMO",
        "project_description": "Say something about DYNAMO",
        "project_url": "",
        "platform": platforms["REVELLE"]["name"],
        "target_sample_rh": "60%",
        # "trajectory_id": "NAAMES-4_RHBrown"
    },
    "CALNEX": {
        "project": "CalNex",
        "project_description": "Say something about calnex",
        "project_url": "",
        "platform": platforms["ATLANTIS"]["name"],
        "target_sample_rh": "60%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "VOCALS": {
        "project": "VOCALS",
        "project_description": "Say something about vocals",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "60%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "ICEALOT": {
        "project": "ICEALOT",
        "project_description": "Say something about icealot",
        "project_url": "",
        "platform": platforms["KNORR"]["name"],
        "target_sample_rh": "25%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "TEXAQS2006": {
        "project": "TexAQS-GoMACCS",
        "project_description": "Say something about texaqs",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "60%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "NEAQS2004": {
        "project": "NEAQS-2004",
        "project_description": "Say something about neaqs2004",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "60%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "NEAQS2002": {
        "project": "NEAQS-2002",
        "project_description": "Say something about neaqs2002",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "ACEASIA": {
        "project": "ACEASIA",
        "project_description": "Say something about aceasia",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "NAURU99": {
        "project": "NAURU-99",
        "project_description": "Say something about nauru99",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "AEROINDO99": {
        "project": "AEROSOLS99-INDOEX",
        "project_description": "Say something about nauru99",
        "project_url": "",
        "platform": platforms["RHBROWN"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "ACE2": {
        "project": "ACE-2",
        "project_description": "Say something about ace2",
        "project_url": "",
        "platform": platforms["VODYANITSKIY"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "CSP": {
        "project": "CSP",
        "project_description": "Say something about csp",
        "project_url": "",
        "platform": platforms["DISCOVERER"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "ACE1": {
        "project": "ACE-1",
        "project_description": "Say something about ace1",
        "project_url": "",
        "platform": platforms["DISCOVERER"]["name"],
        "target_sample_rh": "55%",
        # "trajectory_id": "CalNex_Atlantis"
    },
    "RITS94": {
        "project": "RITS-94",
        "project_description": "Say something about rits94",
        "project_url": "",
        "platform": platforms["SURVEYOR"]["name"],
        # "trajectory_id": "CalNex_Atlantis"
    },
    "RITS93": {
        "project": "RITS-93",
        "project_description": "Say something about rits93",
        "project_url": "",
        "platform": platforms["SURVEYOR"]["name"],
        # "trajectory_id": "CalNex_Atlantis"
    },
    "MAGE92": {
        "project": "MAGE-92",
        "project_description": "Say something about mage92",
        "project_url": "",
        "platform": platforms["VICKERS"]["name"],
        # "trajectory_id": "CalNex_Atlantis"
    },
    "PSI3": {
        "project": "PSI-3",
        "project_description": "Say something about psi3",
        "project_url": "",
        "platform": platforms["DISCOVERER"]["name"],
        # "trajectory_id": "CalNex_Atlantis"
    },
}

# AEROSOLS99-INDOEX
# NAAMES-1
# RITS-93

# imp: add mid-, stop-time