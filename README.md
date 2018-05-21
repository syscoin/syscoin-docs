Syscoin Documentation
===

This repository contains two different kinds of documentation- **[API documentation](https://syscoin.github.io/syscoin-docs/)** for the [Syscoin API](https://github.com/syscoin/syscoin-api) and [Syscoin Core](https://github.com/syscoin/syscoin) as well as **[reference documentation](https://syscoin.readthedocs.io/en/latest/)** for [Syscoin Core](https://github.com/syscoin/syscoin). 

### Quick Reference

 - [Syscoin API Documentation](https://syscoin.github.io/syscoin-docs/)
 - [Syscoin Reference Documentation](https://syscoin.readthedocs.io/en/latest/)

### Note about API Docs
The API docs are generated from the OpenAPI specification defined in [Syscoin API](https://github.com/syscoin/syscoin-api). The [Syscoin API](https://github.com/syscoin/syscoin-api) project is a Node/Express layer for interacting with [Syscoin Core](https://github.com/syscoin/syscoin) using REST. The same APIs are available via [Syscoin Core](https://github.com/syscoin/syscoin) directly using the built in [RPC Server](https://en.bitcoin.it/wiki/API_reference_%28JSON-RPC%29#JSON-RPC).

Building API Docs Locally
===

### Prerequisites

You're going to need:

 - **Linux or OS X** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up

1. Fork this repository on GitHub.
2. Clone *your forked repository* (not our original one) to your hard drive with `git clone https://github.com/YOURUSERNAME/syscoin-docs.git`
3. `cd syscoin-docs`
4. Initialize and start Syscoin-docs. You can either do this locally, or with Vagrant:

```shell
# either run this to run locally
bundle install
bundle exec middleman server

# OR run this to run with vagrant
vagrant up
```

You can now see the docs at http://localhost:4567. Whoa! That was fast!

### Converting OpenAPI to Markdown

For converting OpenAPI specs to Markdown the excellent [Widdershins](https://github.com/mermade/widdershins) converter is suggested. The output should be saved to `source/index.html.md`.

Contributors
===
Improve these docs through pull requests to be added as a contributor.

Special Thanks
---
- [Slate](https://github.com/lord/slate)
