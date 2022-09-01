def run(*args, **kwargs):
    '''
    run is entry point for the service
    '''
    print("[START] Service Begin")

    print(f"Processing: {kwargs['data']}")

    # TODO: replace the following cide with actual service code
    # currently sleeping for 10s, to demonstrate a long running process.
    from time import sleep
    sleep(20)

    print("[DONE] Service Completed")
