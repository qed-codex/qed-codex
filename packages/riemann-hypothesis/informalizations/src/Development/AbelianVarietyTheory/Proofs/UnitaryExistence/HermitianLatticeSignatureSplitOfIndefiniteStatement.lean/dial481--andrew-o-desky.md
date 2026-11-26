---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/HermitianLatticeSignatureSplitOfIndefiniteStatement.lean",
  "declarations": [
    "GlobalTheory.T.hermitianLatticeSignatureSplit_of_indefinite"
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

## An indefinite polarized CM lattice splits by signature

[Theorem AV.0926](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitianLatticeSignatureSplit_of_indefinite/)

Fix the CM host and polarized-lattice conditions described below. Suppose a polarized lattice datum of signature $(1,0)$ exists for this host. Let $(\Lambda,E_0)$ be another such datum of signature $(p,q)$ with $p,q\ge1$ and $p+q\ge3$. There are $\mathcal O_E$-submodules $\Lambda_+,\Lambda_-\subseteq\Lambda$ with $$\Lambda_++\Lambda_-=\Lambda,\qquad E_0(\Lambda_+,\Lambda_-)=0,\qquad\operatorname{rk}\Lambda_+=p,\quad\operatorname{rk}\Lambda_-=q,$$ and, for nonzero vectors in the indicated submodules, $$\operatorname{Im}(r_0)E_0(rx,x)>0\quad(x\in\Lambda_+),\qquad\operatorname{Im}(r_0)E_0(rx,x)<0\quad(x\in\Lambda_-).$$
