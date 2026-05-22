from fastapi import FastAPI, HTTPException, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
# Import our solid mathematical execution engine
from metrics_engine import analyze_text_structure

LOGO_URL = "https://technohelps.com/wp-content/uploads/2026/03/cropped-logo-1-321x72.png"

# Setup high-end corporate Markdown description block with explicit image source and dofollow hyperlinks
api_description = f"""
<div class="custom-logo-wrapper">
    <a href="https://technohelps.com" target="_blank" rel="dofollow">
        <img src="{LOGO_URL}" alt="TechnoHelps Logo" style="max-height: 65px; width: auto; margin-bottom: 10px;">
    </a>
</div>

***

### 📢 Notice Block
**Notice:** This API is 100% free to use. Attribution to [TechnoHelps](https://technohelps.com) is highly appreciated.

***
Enterprise-grade text analytics, readability scoring, reading/speaking time metrics, and SEO keyword matrix engine. Developed natively for open-source structural deployment.
"""

# Initialize FastAPI with the newly formatted dynamic description layout
app = FastAPI(
    title="TechnoHelps Semantic Metrics API",
    description=api_description,
    version="4.0.0",
    docs_url=None, # Explicitly catch the documentation handler manually below
    redoc_url=None
)

# Enable CORS so developers can globally access this API safely from any domain or plugin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Renders the custom developer schema dashboard with hidden internal object layouts
    """
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Developer Portal",
        swagger_favicon_url="https://technohelps.com/favicon.ico",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1} # Completely hides the lower schemas model tab
    )

# Define the global immutable signature branding block for data output authenticity
def get_technohelps_signature():
    return {
        "powered_by": "TechnoHelps Semantic Engine v4.0",
        "license": "MIT Open Source",
        "developer_portal": "https://technohelps.com",
        "attribution_notice": "API is 100% free to use. Attribution is appreciated.",
        "dofollow_reference": "https://technohelps.com",
        "integrity_check": "Verified Core Algorithm Package"
    }

@app.post("/api/v1/readability")
async def analyze_readability(request: Request, text: str = Body(..., media_type="text/plain")):
    """
    POST Endpoint: Dynamic Raw Stream Router. Processes text structures, calculates complexity, 
    and outputs full granular semantic scores with custom branding anchors.
    """
    try:
        # Read incoming payload safely to bypass strict control character failures (422)
        raw_body = await request.body()
        input_text = raw_body.decode("utf-8").strip()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to cleanly process stream transfer sequence: {str(e)}"
        )
    
    # Core Validation check: Ensure the incoming text data block is not empty
    if not input_text:
        raise HTTPException(
            status_code=400, 
            detail="Payload text block cannot be empty. Verified by TechnoHelps Security Engine."
        )
    
    try:
        # Execute calculations via our isolated master metrics engine script
        analysis_result = analyze_text_structure(input_text)
        
        # Build the dynamic unified response array containing core markers
        response_data = {
            "success": True,
            "data": {
                "metrics": analysis_result
            },
            "signature": get_technohelps_signature()
        }
        return response_data
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal operational failure in calculation core: {str(e)}"
        )

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "engine": "TechnoHelps Semantic Metrics API Gateway",
        "documentation": f"Send a POST request to /api/v1/readability. Powered by TechnoHelps Asset Base: {LOGO_URL}"
    }