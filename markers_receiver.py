from pylsl import StreamInlet, resolve_stream, LostError

def main():
    print("looking for our Markers stream...")
    streams = resolve_stream("name", "labvanced_stream_1")
    inlet = StreamInlet(streams[0])
    while True:
        try:
            sample, timestamp = inlet.pull_sample(timeout=1.0)
            if timestamp is not None:
                print(timestamp, sample)
        except LostError:
            print("Lost connection to Labvanced. Exiting...")
            break

if __name__ == '__main__':
    main()
