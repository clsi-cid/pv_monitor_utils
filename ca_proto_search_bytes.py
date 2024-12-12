import struct

# import from pv monitor repo
from PVMonitor_gateway.definitions_gw import EPICS

def ca_proto_search_bytes(cid, pv_name):
        """Helper function for handle_cmd_ca_proto_search that generates UDP
        bytes for broadcasting. 
        NOTE: !!!DO NOT change this code!!!
        """
        pv_len = len(pv_name)

        # Padding
        pad_len = 8 - (pv_len % 8)
        
        payload_len = pv_len + pad_len

        # Format the CA_PROTO_SEARCH UDP packet to send
        # breem:2021_08_10: Turns out EPICS V7 apps need a CA_PROTO_VERSION
        # packet in the same datagram
        # fmt = "!HHHHLL%ds%dx" % (pv_len, pad_len)
        fmt = "!HHHHLLHHHHLL%ds%dx" % (pv_len, pad_len)
        
        # m = struct.pack(fmt, EPICS.CA_PROTO_SEARCH, payload_len,
        #     EPICS.DONT_REPLY, EPICS.CA_CLIENT_MINOR_PROT_VER,
        #     self._cid, self._cid, pv_name)
               
        m = struct.pack(fmt, EPICS.CA_PROTO_VERSION, 0, 1, EPICS.CA_CLIENT_MINOR_PROT_VER, 0, 0,
            EPICS.CA_PROTO_SEARCH, payload_len,
            EPICS.DONT_REPLY, EPICS.CA_CLIENT_MINOR_PROT_VER,
            cid, cid, pv_name)
        
        return m, pv_len, pad_len, payload_len, fmt
    
if __name__ == "__main__":
    print(ca_proto_search_bytes(1000, b"Test"))