# Bookstacks PDF publications

This repository publishes the generated PDF editions used by
[Bookstacks](https://bookstacks.org). Canonical TEI and the website remain in
[ianrastall/bookstacks](https://github.com/ianrastall/bookstacks).

Each edition under `books/<author>/<edition>/` has a `-light.pdf` and a
`-dark.pdf`, plus individual checksum manifests. The root `manifest.json`
records the source repository revision, canonical edition identity, text
language, source XML checksum, PDF checksums and page counts. The two variants
must have identical page counts and extracted text.

Bookstacks embeds these files with its own PDF.js widget. Its Read online
option continues to use responsive HTML; Read PDF keeps the fixed PDF layout.
The embedded PDF follows the website's light/dark theme. No separate domain,
PDF rendering service or visitor-facing conversion backend is required.

## Publish

PDF generation is an explicit offline operation in the source repository:

```powershell
$env:BOOKSTACKS_EXPORT_ROOT = 'D:/jupiter/bookstacks-pdf/books'
python D:/jupiter/bookstacks/scripts/build_exports.py --all --theme both --workers 4
```

The source repository's publication-index command validates the pair, writes
the root manifest here and updates the versioned website index. Commit the PDF
publication first, verify its Pages deployment, then publish the website's
matching manifest snapshot. TEI imports, PDF generation, and site deployment
remain separate operations.

GitHub Pages serves the validated `books/` files. The deployment workflow does
not fetch TEI, run the exporter, or rebuild PDFs. Run `python scripts/build_site.py`
to check the manifest and create `_site/` locally.

## Rights

The source and rights record within each PDF and its canonical TEI applies to
that edition. Bookstacks adds no blanket restriction to the underlying works.
Fonts are embedded as publication subsets; font notices and source records are
maintained with the exporter in the main repository.
