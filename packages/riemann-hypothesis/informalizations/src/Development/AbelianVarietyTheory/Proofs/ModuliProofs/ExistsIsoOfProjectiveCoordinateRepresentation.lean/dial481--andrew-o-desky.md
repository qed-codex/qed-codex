---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsIsoOfProjectiveCoordinateRepresentation.lean",
  "declarations": [
    "GlobalTheory.RepUniq.exists_iso_of_projRep"
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

## Uniqueness of a scheme representing projective coordinates

[Theorem AG.0700](https://andrewodesky.com/rh/lean/GlobalTheory.RepUniq.exists_iso_of_projRep/)

Let $R$ be a commutative ring, $I$ a set, and $J,J'\subset R[X_i:i\in I]$ ideals. Let $Z,Z'$ be $R$-schemes with line bundles $M,M'$ and sections $(\theta_i),(\theta_i')$. Suppose each triple represents its ideal's projective coordinate equations in the sense below. Assume that, for every commutative $R$-algebra $R'$ and every tuple $v\in(R')^I$ generating the unit ideal, $$F(v)=0\ (F\in J)\quad\Longleftrightarrow\quad F(v)=0\ (F\in J').$$ Then there is an $R$-isomorphism $e:Z\to Z'$ and an isomorphism $M\simeq e^*M'$ such that, for every commutative ring $R'$, $x:\operatorname{Spec}R'\to Z$, and $v\in(R')^I$, the tuple $v$ is a system of coordinates for $(M,\theta,x)$ if and only if it is one for $(M',\theta',e\circ x)$.
