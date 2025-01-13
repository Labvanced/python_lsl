from pylsl import pylsl, StreamInfo, StreamInlet, StreamOutlet, resolve_stream, LostError
import math
def main():
    print("creating mouse response stream...")
    info = StreamInfo(name='mouse_response', 
                      type='Mouse', 
                      channel_count=2, 
                      nominal_srate=0, 
                      channel_format=pylsl.cf_int64, 
                      source_id='myuidw43536',
                      )
    outlet = StreamOutlet(info)
    print("looking for our input stream...")
    stream_marker = resolve_stream("name", "labvanced_marker")
    print("found marker stream")
    stream_mouse = resolve_stream("name", "labvanced_mouse")
    print("found mouse stream")
    inlet_marker = StreamInlet(stream_marker[0])
    inlet_mouse = StreamInlet(stream_mouse[0])
    while True:
        try:
            marker_val, timestamp = inlet_marker.pull_sample(timeout=0.0)
            if timestamp is not None:
                print(f"Received Marker with timestamp: {timestamp} and string: {marker_val}")
            mouse_coord, timestamp = inlet_mouse.pull_sample(timeout=0.0)
            if timestamp is not None:
                print(f"Received Mouse with timestamp: {timestamp} and coordinates: {mouse_coord}")
                # Sending it back to Labvanced as int64
                if not (math.isnan(mouse_coord[0]) or math.isnan(mouse_coord[1])):
                    outlet.push_sample([int(mouse_coord[0]), int(mouse_coord[1])])
        except LostError:
            print("Lost connection to Labvanced. Exiting...")
            break

if __name__ == '__main__':
    main()
