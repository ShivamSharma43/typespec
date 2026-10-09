---
changeKind: fix
packages:
  - "@typespec/http-client-python"
---

Fix `IndexError` crash when the TypeSpec program has nothing to generate (for example a service with only an empty interface). The package is now laid out under the service namespace.
