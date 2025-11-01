from flask import render_template, Blueprint

bc_bp = Blueprint('blockchain', __name__)

@bc_bp.route('/blockchain_developer/internships')
def blockchain_internships():
    internships = [
        {
            "company": "Polygon",
            "role": "Blockchain Intern",
            "title": "Smart Contract Intern at Polygon",
            "description": "Develop and audit smart contracts for the Polygon network.",
            "requirements": "Solidity, Ethereum, Hardhat, JavaScript.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://polygon.technology/careers"
        },
        {
            "company": "WazirX",
            "role": "Blockchain Developer Intern",
            "title": "Blockchain Intern at WazirX",
            "description": "Build tools and services for crypto wallet integration and trading systems.",
            "requirements": "Node.js, Web3.js, Solidity.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://wazirx.com/careers"
        },
        {
            "company": "CoinDCX",
            "role": "Smart Contract Intern",
            "title": "Blockchain Intern at CoinDCX",
            "description": "Develop smart contract-based features and test DeFi protocols.",
            "requirements": "Solidity, Truffle, JavaScript.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://coindcx.com/careers"
        },
        {
            "company": "ZebPay",
            "role": "Blockchain Analyst Intern",
            "title": "Blockchain Intern at ZebPay",
            "description": "Analyze transaction patterns and write scripts to trace smart contract behavior.",
            "requirements": "Python, Blockchain APIs, Solidity (bonus).",
            "location": "Ahmedabad, Gujarat",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "4 months",
            "apply_link": "https://zebpay.com/careers"
        },
        {
            "company": "Unocoin",
            "role": "Crypto Intern",
            "title": "Blockchain Developer Intern at Unocoin",
            "description": "Assist in building crypto exchange tools and blockchain data services.",
            "requirements": "Go/Rust, APIs, Web3.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.unocoin.com/careers"
        },
        {
            "company": "EPNS (Push Protocol)",
            "role": "Blockchain Tech Intern",
            "title": "Smart Contract & Protocol Intern",
            "description": "Work on blockchain notifications protocol and decentralized messaging tools.",
            "requirements": "Solidity, Graph Protocol, React.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "4 months",
            "apply_link": "https://push.org/careers"
        },
        {
            "company": "OpenSea",
            "role": "Engineering Intern",
            "title": "Blockchain Developer Intern at OpenSea",
            "description": "Help build infrastructure for NFTs, metadata processing, and on-chain interactions.",
            "requirements": "Solidity, Ethers.js, TypeScript.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://opensea.io/careers"
        },
        {
            "company": "Persistence",
            "role": "Cosmos Blockchain Intern",
            "title": "Full Stack Blockchain Intern",
            "description": "Contribute to dApps and staking platforms built on Cosmos SDK.",
            "requirements": "Cosmos, Rust, React.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://persistence.one/careers"
        },
        {
            "company": "BitsCrunch",
            "role": "Blockchain Research Intern",
            "title": "Blockchain Analyst Intern at BitsCrunch",
            "description": "Research NFT patterns and build tools to detect fraud and wash trading.",
            "requirements": "Data Analysis, Smart Contract basics, Python.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://bitscrunch.com/careers"
        },
        {
            "company": "Chainsafe",
            "role": "Distributed Systems Intern",
            "title": "Blockchain Protocol Intern",
            "description": "Work on Ethereum 2.0 and Filecoin-based infrastructure projects.",
            "requirements": "Rust, Golang, IPFS, Distributed systems.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://chainsafe.io/careers"
        },
        {
        "company": "Tata Consultancy Services (TCS)",
        "role": "Blockchain R&D Intern",
        "title": "Blockchain Intern at TCS Research Labs",
        "description": "Research and develop blockchain-based enterprise solutions in supply chain and identity management.",
        "requirements": "Hyperledger Fabric, Ethereum, Java, REST APIs.",
        "location": "Pune, Maharashtra",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://www.tcs.com/careers"
    },
    {
        "company": "Tech Mahindra",
        "role": "Blockchain Intern",
        "title": "DLT Intern at Tech Mahindra",
        "description": "Work on DLT implementations and integrations with enterprise-grade applications.",
        "requirements": "Corda/Quorum, Blockchain APIs, Java.",
        "location": "Hyderabad, Telangana",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://careers.techmahindra.com"
    },
    {
        "company": "Infosys",
        "role": "Blockchain Solutions Intern",
        "title": "Blockchain Developer Intern at Infosys",
        "description": "Join the blockchain innovation team and prototype decentralized use cases.",
        "requirements": "Ethereum, Solidity, Web3.js, SQL.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "2 months",
        "apply_link": "https://www.infosys.com/careers"
    },
    {
        "company": "Accenture",
        "role": "Technology Intern - Blockchain",
        "title": "Blockchain Engineering Intern at Accenture",
        "description": "Develop blockchain-based enterprise POCs and smart contract auditing tools.",
        "requirements": "Solidity, Node.js, APIs, Cloud.",
        "location": "Gurugram, Haryana",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://www.accenture.com/in-en/careers"
    },
    {
        "company": "Huddle01",
        "role": "Blockchain + WebRTC Intern",
        "title": "Decentralized Video Intern at Huddle01",
        "description": "Contribute to decentralized audio/video infra using smart contracts and IPFS.",
        "requirements": "Solidity, WebRTC, IPFS.",
        "location": "Remote",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://huddle01.com/careers"
    },
    {
        "company": "Devfolio",
        "role": "Blockchain Community Intern",
        "title": "Blockchain + DevRel Intern at Devfolio",
        "description": "Help build dev tooling and organize community hackathons in Web3 space.",
        "requirements": "Solidity, Ethereum Tooling, Excellent Communication.",
        "location": "Remote",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://devfolio.co/careers"
    },
    {
        "company": "Ocean Protocol",
        "role": "Smart Contract Intern",
        "title": "Blockchain Intern at Ocean Protocol",
        "description": "Work on decentralized data exchange protocols and smart contract testing.",
        "requirements": "Solidity, Python, Brownie/Hardhat.",
        "location": "Remote",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://oceanprotocol.com/careers"
    },
    {
        "company": "Instadapp",
        "role": "Full Stack Blockchain Intern",
        "title": "Blockchain Intern at Instadapp",
        "description": "Contribute to DeFi dashboards and smart contract integrations.",
        "requirements": "React, Web3.js, Solidity, Ethers.js.",
        "location": "Remote",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://instadapp.io/careers"
    }
]

    return render_template('bc_internships.html', internships=internships)
