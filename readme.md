# Interception of VoIP calls on G711 encoding

## Introduction


The purpose of the software is to carry out an eavesdropping attack on a VoIP call over the RTP protocol, thus making the communication listenable to everyone.

----------------------------------------------------------------------------------------------------------------------------

**The libraries and tools used in the software are:**
 - **Pyshark:**  The Pyshark library underpins how the software works as its own
through it we can read the packages from the .pcap file. 
More information on the official [repository](https://github.com/KimiNewt/pyshark/)
 - **SoX (Sound eXchange):** Provides all possible operations that can be performed on audio data, from manipulation, from the playback of the recording. In detail it reads and writes in multiple formats disseminated and may possibly apply effects on them.
 More information on the official [page](https://sox.sourceforge.net/)
 - [**Wireshark**](https://www.wireshark.org/) and [**tshark**](https://www.wireshark.org/docs/man-pages/tshark.html)

----------------------------------------------------------------------------------------------------------------------------

## Software

The software consists of six functions (**readfile**, **control_int**, **listen**,
**def_source**, **def_codec** e **decode**) plus a main part. As you can see from the function names:
1. **readfile**: will read the pcap file;
2. **control_int**: will do a type check of the passed data needed for correct software operation;
3. **listen**: will have the function of making it possible to listen to the created wav files;
4. **def_source**: will define the source or the sources of the call;
5. **def_codec**: will define the codec used;
6. **decode**:  will take care of decoding it.

----------------------------------------------------------------------------------------------------------------------------

## Usage

Run the program [**eavesdropping.py**](https://github.com/GiuseppeGalante/RTP_EavesdroppingAttack_Example/blob/main/eavesdropping.py) with:
`python3 prog.py`
and follow the program instructions.