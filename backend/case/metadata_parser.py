from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core.tools import makePrintable

def extract_video_metadata(file_path: str) -> dict:
    """
    Extract metadata from a video file using Hachoir.
    Returns a dictionary of metadata key/value pairs.
    """
    parser = createParser(file_path)
    if not parser:
        raise ValueError(f"Unable to parse file: {file_path}")
    
    metadata = extractMetadata(parser)
    if not metadata:
        return {}

    return {
        makePrintable(key, key_is_text=True): makePrintable(str(value), value_is_text=True)
        for key, value in metadata.exportDictionary().items()
    }
