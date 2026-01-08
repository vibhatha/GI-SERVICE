#!/usr/bin/env python
"""
Test script to verify the opendata package installation and imports.
"""

import sys
from pathlib import Path

# Add current directory to path for testing before installation
current_path = Path(__file__).parent
sys.path.insert(0, str(current_path))

def test_imports():
    """Test that all main imports work correctly."""
    print("Testing opendata package imports...")
    print("=" * 60)
    
    try:
        # Test main package import
        import opendata
        print("✅ Successfully imported opendata")
        print(f"   Version: {opendata.__version__}")
        print(f"   Author: {opendata.__author__}")
        
        # Test model imports
        from opendata import ENTITY_PAYLOAD, ATTRIBUTE_PAYLOAD, WRITE_PAYLOAD
        print("✅ Successfully imported models")
        
        # Test service imports
        from opendata import (
            IncomingServiceAttributes,
            IncomingServiceOrgchart,
            WriteAttributes,
        )
        print("✅ Successfully imported services")
        
        # Test dependency imports
        from opendata import get_config
        print("✅ Successfully imported dependencies")
        
        # Test that we can instantiate services
        config = {
            "BASE_URL_CRUD": "http://test:8080",
            "BASE_URL_QUERY": "http://test:8081"
        }
        
        attr_service = IncomingServiceAttributes(config)
        print("✅ Successfully instantiated IncomingServiceAttributes")
        
        org_service = IncomingServiceOrgchart(config)
        print("✅ Successfully instantiated IncomingServiceOrgchart")
        
        write_service = WriteAttributes()
        print("✅ Successfully instantiated WriteAttributes")
        
        print("=" * 60)
        print("🎉 All imports successful! Package is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)

