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
          "xcode_settings": {
            "MACOSX_DEPLOYMENT_TARGET": "10.10",
            "OTHER_CFLAGS": [
              "-Wall",
              "-Werror",
              "-Wno-deprecated-declarations"
            ]
          },
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
