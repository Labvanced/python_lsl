import time
from pylsl import StreamInfo, StreamOutlet
from pylsl.pylsl import cf_string

def main():
    info = StreamInfo(name='my_stream_1', 
                      type='Markers', 
                      channel_count=1, 
                      nominal_srate=0, 
                      channel_format=cf_string, 
                      source_id='myuidw43536',
                      )
    outlet = StreamOutlet(info)
    while True:
        text_to_send = input("Enter the text to send (or 'exit' to quit): ")
        if text_to_send.lower() == 'exit':
            break
        print("sending marker %s" % text_to_send)
        outlet.push_sample([text_to_send])

if __name__ == '__main__':
    main()
