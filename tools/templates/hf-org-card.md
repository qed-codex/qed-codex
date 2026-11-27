---
title: README
emoji: 📖
colorFrom: gray
colorTo: blue
sdk: static
pinned: false
---

# QED Codex

QED Codex is an open directory of machine-written Lean proofs. Each file and each declaration has a page. The page shows explanations in plain mathematical language, written by people and by AI, side by side.

- Site: https://qedcodex.org
- Source and contributions: https://github.com/qed-codex/qed-codex
- Guide for AI agents: https://qedcodex.org/llms.txt

## What is here

[qed-codex/qed-codex](https://huggingface.co/datasets/qed-codex/qed-codex) is a copy of the directory's database as Parquet tables: the proofs, their modules and declarations, the import graph, the recorded trails to the main theorems and the text that may be redistributed. Its dataset card gives the current counts and the licence of each part. The same data is published as one SQLite file with each [GitHub release](https://github.com/qed-codex/qed-codex/releases).

Text that the site shows by permission only is not in this copy. That covers Andrew O'Desky's statements of the Lean Riemann Hypothesis project. They can be read on the site and on his own page.

## Credit

The proofs belong to their authors. The directory builds on Levent Alpöge's formalization of the Riemann Hypothesis, the readable rewrite published by Luke Sernau, the Lean developments published by Anthropic and OpenAI, James Shore's dependency data built from Andrew Sutherland's kernel export, and Andrew O'Desky's statements. Each page names its sources and pins them to a commit.

QED Codex does not verify proofs. Where a verification record exists for a proof, its page links to it. The project is independent and is not affiliated with any AI vendor.

## Take part

Anyone can add an explanation of a file through a pull request. New text is CC BY 4.0. Start on any module page at https://qedcodex.org or read [CONTRIBUTING.md](https://github.com/qed-codex/qed-codex/blob/main/CONTRIBUTING.md).

Contact: contact@qedcodex.org