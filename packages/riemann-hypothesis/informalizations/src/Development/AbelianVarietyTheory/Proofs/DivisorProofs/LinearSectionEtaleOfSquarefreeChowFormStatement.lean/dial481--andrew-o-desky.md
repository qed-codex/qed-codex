---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LinearSectionEtaleOfSquarefreeChowFormStatement.lean",
  "declarations": [
    "GlobalTheory.T.linearSection_etale_of_squarefree_chowForm"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A squarefree specialized Chow form detects a finite etale section

[Theorem AG.0702](https://andrewodesky.com/rh/lean/GlobalTheory.T.linearSection_etale_of_squarefree_chowForm/)

Let $F$ be a number field and let $Y/F$ be smooth, projective and geometrically connected of dimension $D\ge1$. Let $L$ be a line bundle with $F$-linearly independent sections $b_1,\ldots,b_N$ having no common zero. Include the source's auxiliary Hermitian-system data: a spanning matrix of section combinations, arbitrary matrices at complex embeddings, a closed boundary $B\ne Y$, an integer $j_0\ge0$ and a section of $L^{j_0}$. Write $I$ for the homogeneous ideal of the projective image of $(b_j)$. Let $\delta\ge0$ equal the top self-intersection $L^D$, and let $f$ be its Chow form with $D+1$ coefficient blocks and degree $\delta$ in each block.

Let $E/F$ be any field extension and $s_1,\ldots,s_D\in E^N$. Suppose the common zero scheme $Z$ of $\sum_j s_{ij}b_j$ has finite support and lies in $(Y\setminus B)_E$. Let $f_s\in\overline E[U_1,\ldots,U_N]$ be obtained by substituting the $s_i$ into the first $D$ blocks of $f$. If $f_s\ne0$ and no square of a nonconstant linear form divides $f_s$, then $Z/E$ is finite etale, $Z(\overline E)$ has exactly $\delta$ points, their projective images are distinct, and $$f_s(U)=c\prod_{z\in Z(\overline E)}\sum_j U_j b_j(z)\qquad(c\in\overline E^\times),$$ using any nonzero homogeneous coordinates $(b_j(z))$ for each image.
