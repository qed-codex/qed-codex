---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/UnifPreCharacterGroupIso.lean",
  "declarations": [
    "GlobalTheory.unifPre_characterGroup_iso"
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

## Comparison of the character lattices of two uniformizations

[Theorem AV.0675](https://andrewodesky.com/rh/lean/GlobalTheory.unifPre_characterGroup_iso/)

Let $R$ be a noetherian integrally closed local domain, let $I\subseteq R$, and assume $R$ is $I$-adically complete. Let $D,D'$ be degeneration data, let $A,A'$ be polarized abelian varieties over $\operatorname{Frac}R$, and let $G$ be a commutative semiabelian scheme over $R$. Suppose preliminary uniformizations $U,U'$ identify its generic fibre with $A,A'$ and realize $D,D'$ on every thickening $R/I^{e+1}$. Write $X_D,X_{D'}$ for their character groups, $B,B'$ for their abelian parts, and $p_e:G_e\to B$, $p'_e:G_e\to B'$ for their maps on each thickening.

There is an additive isomorphism $a:X_{D'}\simeq X_D$ with the following property. For every $e\ge0$, scheme $Z$, map $r:Z\to G_e$, and point $z\in Z$, suppose both $p_e r$ and $p'_e r$ factor through the respective identity sections over the base. Choose, for each map from $Z$ to $B$ or $B'$, a line-bundle chart containing the image of $z$. For every $x\in X_{D'}$, the scalar germs in $\mathcal O_{Z,z}^{\times}$ obtained by evaluating the two torus-coordinate generators satisfy $$t_{a(x)}(r)_z=t'_x(r)_z.$$
