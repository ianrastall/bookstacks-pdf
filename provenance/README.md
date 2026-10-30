# Export provenance

The exporter snapshots preserve the exact script bytes used during this
publication run, including the initial batch and the glyph/illustration fixes.
They are documentary copies; the maintained exporter lives in
`ianrastall/bookstacks/scripts/build_exports.py`. To reproduce a historical
batch, restore the corresponding snapshot at that path in the source checkout,
install its recorded dependencies, and fetch the hash-pinned font resources.

Every PDF's individual manifest records its generator fingerprint and source
XML hash. The root publication manifest records the canonical source commit,
all PDF checksums and the matching text/page checks. Font provenance and license
references are in `font-resources.json`; original source font files remain
outside this publication repository. All available source illustrations are
embedded into their PDFs; no canonical image assets or TEI are changed here.

The western-punctuation snapshot corrects xeCJK quote classes for English
editions with incidental Han characters; both themes of the seven affected
editions were explicitly regenerated and visually checked.

The drama-layout snapshot records the 29 October 2026 Shakespeare update and
17 newly published Christie pairs. The matching `drama_layout.py`, movement
rules and source-pinned character index accompany it. Restore those files to
their original paths in the source checkout for reproduction; the source
commit is recorded in the root manifest. All 102 regenerated/new dark editions
were checked for opaque black text, and representative pages in both themes
were rendered for visual inspection.
