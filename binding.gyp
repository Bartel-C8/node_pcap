{
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ['OS == "mac"', {
          "link_settings": {
            "libraries": [
              "-lpcap"
            ]
          }
        }]
      ]
    }
  ]
}
