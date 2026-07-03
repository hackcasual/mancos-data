# mancos-data

Prebuilt modpack bundles served to the [Mancos](https://github.com/hackcasual/mancos)
factory planner via GitHub Pages. The app fetches `bundles/manifest.json`
from this repo's Pages site; the manifest is regenerated on every deploy
from whatever `.yafcbundle` files are in `bundles/`.

To add a pack: build a bundle with the Mancos bundler (web page or
`yafc_bundler` CLI), drop it in `bundles/`, and push.

Bundles contain data and icons derived from Factorio and the bundled mods;
they are hosted here for personal use of this deployment.
