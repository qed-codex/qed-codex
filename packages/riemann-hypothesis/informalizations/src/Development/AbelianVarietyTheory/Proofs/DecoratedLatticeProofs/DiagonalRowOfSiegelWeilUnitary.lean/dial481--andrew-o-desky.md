---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitary.lean",
  "declarations": [
    "GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary"
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

## Hilbert-Schmidt bound for the normalized Gram operator of a source, assuming the Siegel-Weil formula

[Theorem THETA.1.1759](https://andrewodesky.com/rh/lean/GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary/)

Assume ([Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)). Let $C_g,c_b,C_u,c_T,C_T$ be real numbers with $c_b>0$ and $c_T>0$. Then there are real numbers $C\ge1$, $C'_0$ and $C_{\ell,0}$ such that the following holds for all real numbers $C'\ge C'_0$ and $C_\ell\ge C_{\ell,0}$.

Let $D$ be a datum, $L$ a real number and $z$ a source of $D$. Suppose that $D$ satisfies the standing conditions of the diagonal estimate at scale $L$ with constants $(C',C_\ell,C_g,c_b,C_u,c_T,C_T)$. Then the normalized Gram operator $K_z$ of $z$ satisfies $$\bigl\|K_z-\mathrm{id}\bigr\|_{\rm HS}^2\ \le\ 4\bigl(e^{C\,m^5fL}+1\bigr)\,\frac{d_z^{\,2}}{D_*}\;+\;\bigl(4\,e^{-\frac12kf\log k}+2\,e^{-kf\log k}\bigr)\,d_z .$$

The datum and its sources, the operator $K_z$ on the Hilbert space $C_z$ of dimension $d_z$, the integers $k,m,f$, the positive real number $D_*$ and the standing conditions are defined in ([Normalized Gram operators and the standing conditions of the diagonal estimate](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Kmat/)).
