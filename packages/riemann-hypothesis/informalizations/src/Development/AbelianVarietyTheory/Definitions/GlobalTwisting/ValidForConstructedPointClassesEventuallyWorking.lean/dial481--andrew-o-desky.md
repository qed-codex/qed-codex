---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean",
  "declarations": [
    "GlobalTheory.Fc.Row"
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

## Points of the construction, properties of points, attached records and statements over families

[Definition / hypothesis THETA.D064](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.Row/)

This page explains the scheme in which statements about the whole construction are phrased. A statement in this scheme has the form "eventually in the parameters, at every point with a given property, a record with given properties exists (or: every linked record has a given property)". The terms are as follows; "context", "base", "frame", "twist data" and "eventually" are as in ([Contexts, and statements that hold eventually in the parameters](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.EvG/)), and "datum" and "object" as in ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)).

**Stages and points.** Over a base $B$ the rest of a datum is chosen in six successive steps, each a record depending on the earlier ones. The seven records $X=(B,X_1,\dots,X_6)$ are the *stages*, and they assemble into a datum $D(X)$. A *core* at a context $\mathcal{K}$, stages $X$, a frame $f$ and twist data $T$ is a record certifying that these fit together: it contains characters $\xi_\mu$ of $E$ indexed by the tuples of $D(X)$ (pairwise distinct, with $\xi_{\mu_0}=1$ and with the twisted characters of $T$ among them), a set of places of $\mathbb{L}$ at which the twist is active, a record of auxiliary choices, and about twenty conditions tying $D(X)$ to the scale and the constants of $\mathcal{K}$. A *point* at $\mathcal{K}$ consists of stages, a frame, twist data and a core, together with size data and further choices subject to validity conditions; a point $\beta$ determines a datum $D_\beta$ and an object $O_\beta$ over it.

**Properties of points.** A *property of points* is any predicate $Q(\mathcal{K},X,f,T,c)$ of a context, stages, a frame, twist data and a core $c$.

**Points built by the recipe.** One fixed way of producing stages is singled out: a *column input* for $(B,f,T)$ determines the first later stage, and a choice of the remaining five completes it. A core is *built by the recipe* if it arises in this way and carries a certificate of that fact (compatibility of its components with the column input, about twenty items). The certificate has four places at which further data may be required: a *choice of extensions* $\mathcal{S}$ is a rule giving, for each of the four places, a type depending on the data built so far, and a core is *built with extensions $\mathcal{S}$* if its certificate contains an element of each of the four types. Each condition on built cores defines a property of points: it holds at $(\mathcal{K},X,f,T,c)$ when $X$ and $c$ come from a column input and later stages satisfying the condition.

**Attached records and links.** A *type of attached records* assigns to every datum $D$, object $O$ over $D$ and real number $c$ a type $\mathcal{B}(D,O,c)$. A *link* is a relation between a point $\beta$ at a context, a real number $c$, and an element of $\mathcal{B}(D_\beta,O_\beta,c)$. For a property of points $Q$ and a link:

- *records exist at all $Q$-points* means: eventually in the parameters (second form), for every point $\beta$ at the context with property $Q$ and every real $c$ there is $b\in\mathcal{B}(D_\beta,O_\beta,c)$ linked to $\beta$;
- *a property $E$ of records holds at all linked records* means: eventually in the parameters (second form), for every point $\beta$ with property $Q$, every real $c$ and every $b$ linked to $\beta$, $E(\kappa,D_\beta,O_\beta,c,b)$ holds, where $\kappa$ is the parameter tuple.

**Families and selections.** Use the families in ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), with the shared data in ([Shared data in an arithmetic family](https://andrewodesky.com/rh/s/family-shared-data.html)) and constants in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)). Write $x_1,I_x,D(x,i),L(x,i),J,C_{\rm size}$ for their corresponding components. A *class* $\mathcal A$ is a property of families for every parameter $\varepsilon$.

For $x>x_1$, let $O(x,i)$ be the object assembled from the member's data. A *selection* chooses, for every family $\mathrm{Fm}\in\mathcal A$, every real $x>x_1$ and every $i\in I_x$, a record $$\sigma_{\mathrm{Fm},x,i}\in\mathcal B(D(x,i),O(x,i),C_{\rm size}).$$ The member's scale is then $(x,\varepsilon,J)$.

For comparisons with a context table, use the four ordered-list formulas in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)), replacing the final outgoing entry $\max(C_o,J)$ by the table's $C_8$. The height argument in the middle-list formula is an arbitrary real number.

The selection is *drawn from the $Q$-points with property $E$* if, for each family in $\mathcal A$, there is one parameter tuple $\kappa$ satisfying the following conditions:

- Its exponent is $\varepsilon$, its three numbers $C_5,c_6,C_b$ are positive, and its table is standard.
- Its preliminary and last lists equal the family's corresponding lists; its middle lists agree with the family's middle lists for every real height argument.
- Its outgoing list equals the family's outgoing list after replacing the family's entry $C_T$ by the table's entry $C_T$.
- The family belongs to the fixed basic class of families.
- Every selected datum, object and record is the corresponding datum, object and linked record of some $Q$-point at a context with parameters $\kappa$, and the selected record satisfies $E$.

**Statements over families.** For a property $H$ of selections, *$H$ holds over the $Q$-points* means: there is a property $E$ of records that holds at all linked records, such that $H$ holds for every class of families and every selection for it drawn from the $Q$-points with property $E$. Two forms of $H$ occur: "every chosen record has property $R$", and "a property $P$ of families holds for every family of the class whose constants are large for a threshold depending only on $\varepsilon$, for all $\varepsilon$ below some $\varepsilon_1>0$".
