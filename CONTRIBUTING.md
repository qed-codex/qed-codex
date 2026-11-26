# Contribute an informalization

Enter your GitHub handle and the writer’s credited name on a module page, choose the origin and certify the rights for that origin. **Add an informalization** opens GitHub’s editor. Keep the prefilled source commit and module path and cite the pinned lines. List the declarations discussed when the source has a declaration index. For a source without one, leave `declarations: []` empty.

Choose `wrote` if you wrote the text and name yourself, `generated` if you generated it and name the model, or `other-author` for previously published text, naming the actual writer and giving the source.

Before merging, a maintainer confirms the writer’s name, using the name a person wishes to be credited by or the name a model’s maker publishes, and asks in the pull request if the name is unclear. Before merging an edit to an existing entry, a maintainer confirms that the GitHub account making the edit originally submitted the entry.

Each submitter can contribute one file per writer per module. For example, handle `example` and writer “Example Writer” use `packages/riemann-hypothesis/informalizations/src/Main.lean/example--example-writer.md`. The filename uses Unicode NFKC and lowercase with runs of punctuation or spaces converted to hyphens. Informalizations appear oldest first by their arrival in the ledger. Edits and Git-tracked renames preserve their place. Ties in the same commit use submitter handle, then writer, in binary order. The Permalink beside each informalization uses its submitter and writer, so edits and new submissions preserve the address. A declared agreement uses the target filename stem and the SHA-256 of its complete bytes.

The submitter is responsible for the statement and the right to publish it under the displayed licence. Maintainers may decline or remove any text and will remove it in good faith on a takedown request sent to [contact@qedcodex.org](mailto:contact@qedcodex.org) or when a problem is found.

Keep a public pull request to one package and one module. Each entry may contain up to 256,000 bytes of UTF-8 Markdown, including front matter, and list up to 64 declarations. The checker renders each proposed entry with the site renderer. Its HTML may occupy up to 1,000,000 UTF-8 bytes.

To propose importing a whole proof or many files, identify the source, revision and credits in [Suggest an import](https://github.com/qed-codex/qed-codex/issues/new?template=suggest-import.yml). A maintainer verifies the licence and runs the import.

For a public `other-author` entry, give the published text’s `source`, its `license` (CC-BY-4.0, CC0-1.0, Apache-2.0 or MIT), and the address where that licence is stated in `license_source`. Copy the exact `copyright` line or enter “none in the source”, copy the full `notice` text (use an empty string if absent), and describe `changes` or enter “none”. Before merging, a maintainer opens the stated address and confirms the licence, the copyright line and the notice.

## Flag a problem

Choose **Flag a problem** on the affected module, or open the issue form and enter its original path. Identify the specific informalization, declaration or fact, describe the claim briefly and link the relevant Lean lines or data. The form labels new reports `module-problem`. A maintainer reviews the evidence and adds `dispute` to an open issue that belongs on the module page. The next build shows the issue on the module page. Closing the issue clears it on the following build. [Module problem form](https://github.com/qed-codex/qed-codex/issues/new?template=module-problem.yml)

## Propose an outside link

Add one tab-separated line to `proofs/rh/links.tsv` in a pull request. The columns are `module`, `author`, `url`, `declaration` and `label`. When the outside page explains a named declaration, enter its exact Lean name and the original file that owns it. A page may explain several declarations. Give each one a row and use the author’s title as its label. A module-wide link may leave the declaration empty. Give the fully qualified Lean declaration that justifies the link in the PR description and link to its pinned source line. The compiler checks that the module path exists. A maintainer reviews the declaration evidence. Once the link is merged and the site rebuilds, the entry leaves the unmatched page. [Link ledger](proofs/rh/links.tsv) · [Catalogue cards](proofs/rh/sources/odesky/cards.tsv)

## Licenses and credit

New text written or generated for QED Codex is CC BY 4.0. Previously published text shows its source licence. Imported text keeps its own licence, shown beside it. Code is MIT. A maintainer may import attributed sources under Apache-2.0, MIT or CC0-1.0. These require the original source URL and other-author origin. For Apache-2.0 or MIT, copy the original copyright line verbatim into the copyright field. A maintainer can submit expressly permitted text in the ledger with `origin: other-author`, `license: with-permission`, the writer and the source. It is credited on the site and excluded from the downloadable mirrors. Outside links retain their authors’ terms. [MIT](LICENSE) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · [Seed notice](proofs/rh/seed-license.txt)

Imported entries are never edited by hand. Re-import at a new pin and open a pull request showing the difference. The [import register](imports.tsv) records the pinned inputs and replay commands.
