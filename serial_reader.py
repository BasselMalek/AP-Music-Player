#Reads the latest value from a serial port, decodes it then returns it as a float.
#Created by: Bassel Walid
#Email: bassel.walid04@gmail.com


import sys
import serial


def serial_reader(port_name):
    '''
    Reads the latest value from a serial port, decodes it then returns it as a float
    '''
    
    while True:
        try:
            encoded_value = port_name.readline()
            decoded_value = float(encoded_value[0:len(encoded_value)-2].decode("utf-8"))
        except ValueError:
            print(sys.exc_info())
            continue
        except PermissionError:
            port_name.close()
            print("Port Access error, Please restart script.")
        except:
            print(sys.exc_info())
        else:
            return decoded_value