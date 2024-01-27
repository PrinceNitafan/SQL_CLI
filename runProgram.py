import interfaceHandler

def main():
    running = True
    createInterface = interfaceHandler.InterfaceHandler()

    while running:
        createInterface.currentPage()
        running = createInterface.interfaceRunning()

if __name__ == '__main__':
    main()
