# remsg encode.mjs uint64 Patch

## Problem

The `remsg` package (v1.2.0) has a bug in `dist/encode.mjs` where type 0
attributes are written using `setInt32()` but decoded using `readUint64()`.

This causes `RangeError: The value of "value" is out of range` for sentinel
values (0xFFFFFFFFFFFFFFFF = 18446744073709551615) that cannot fit in int32.

## Affected files

- `node_modules/remsg/dist/encode.mjs`

## Original code (buggy)

```js
case 0:
    encoder.setInt32(entry.attributes[j]);
    break;
```

## Patched code

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

## How to apply

Run `node scripts/utils/patch-remsg.mjs` after `npm install`, or manually
edit `node_modules/remsg/dist/encode.mjs`.
