# remsg encode.mjs Patches

Three bugs were found in `remsg` v1.2.0 `dist/encode.mjs`. All are applied
automatically by `scripts/utils/patch-remsg.mjs` (run via `npm install`).

---

## Bug 1 — uint64 attribute encoding (type 0)

Type 0 attributes were written with `setInt32()` (4 bytes) but decoded with
`readUint64()` (8 bytes), causing silent data corruption.

**Original:**
```js
case 0:
    encoder.setInt32(entry.attributes[j]);
    break;
```
**Fixed:**
```js
case 0: {
    const v = entry.attributes[j];
    if (Number.isSafeInteger(v)) {
        encoder.setInt64(BigInt(v));
    } else {
        encoder.setInt64(-1n);
    }
    break;
}
```

---

## Bug 2 — GMSG magic null terminator (1-byte header shift)

`encoder.setString("GMSG")` writes 5 bytes ("GMSG" + NUL) because
`binary-util`'s `setString` always appends a null terminator. The decoder
reads only 4 bytes for the magic field, causing a 1-byte shift in every
subsequent header field (entryCount, attributeCount, etc.).

**Original:**
```js
encoder.setString("GMSG");
```
**Fixed:**
```js
encoder.setBuffer(Buffer.from("GMSG"));
```

---

## Bug 3 — attributeValues offset captured after write (off-by-8)

The back-fill offset for each attribute value was captured AFTER writing the
placeholder, so back-fills for null (type -1) and string (type 2) attributes
were written 8 bytes too late — overwriting the next attribute instead.

**Original (simplified):**
```js
switch (type) { case -1: encoder.setInt64(-1n); break; ... }
entryHeaderOffsets[i].attributeValues[j] = encoder.currentOffset; // AFTER
```
**Fixed:**
```js
entryHeaderOffsets[i].attributeValues[j] = encoder.currentOffset; // BEFORE
switch (type) { case -1: encoder.setInt64(-1n); break; ... }
```

---

## How to apply

Run `node scripts/utils/patch-remsg.mjs` (or `npm install` which triggers the
postinstall hook).
