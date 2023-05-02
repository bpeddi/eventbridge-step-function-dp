""" This function triggerd by event bridge
"""

def lambda_handler(event, context):
    # pylint: disable=unused-argument
    """Lambda handler"""
    print("This function triggered from event generated from Event Bridge  ---")
    status = dict(status=0)
    return status
