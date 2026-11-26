---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HodgeCrystallineSequences.lean",
  "declarations": [
    "GlobalTheory.HodgeCrysSeq.hodgeExact_at"
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

## Hodge jumps in crystalline lattice sequences

[Theorem PHT.0793](https://andrewodesky.com/rh/lean/GlobalTheory.HodgeCrysSeq.hodgeExact_at/)

Let $\ell$ be prime and fix the compatible local period-ring and integral comparison data of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $K,L$ be finite extensions of $\mathbb Q_\ell$ inside the specified algebraic closure, and let $O_L$ be the valuation ring of $L$. Consider continuous finite-dimensional $L$-representations of the local Galois group of $K$, each equipped with a stable $O_L$-lattice.

For a surjective lattice homomorphism $T_1\to T_2$ between crystalline representations, every Hodge jump of $T_2$ at any embedding $\tau:K\hookrightarrow L$ is a Hodge jump of $T_1$. If $$0\longrightarrow T_0\longrightarrow T_1\longrightarrow T_2\longrightarrow0$$ is exact on the representation spaces and on their lattices, and $T_1$ is crystalline, then $T_0,T_2$ are crystalline and, for every $\tau$ and $a\in\mathbb Z$, $$a\text{ is a jump of }T_1\quad\Longleftrightarrow\quad a\text{ is a jump of }T_0\text{ or }T_2.$$ Finally, every Hodge jump of a trivial lattice representation is zero.
