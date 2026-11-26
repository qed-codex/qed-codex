"""Join explicit Version 2 file citations to the original project's module paths."""
import argparse
import csv
import hashlib
import re
import sqlite3
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

SHA = "e0f49211daeb4156c80f912469c601091f7863418c7b93bea237bae90a9c0500"
PROOF = "40e56bab026552e089d7afcfeff08d2defb9c005"
# Duplicate basenames whose surrounding citation names a declaration in the file.
WITNESSES = {
    (3651,"StatementI"): "ThmAOp", (4741,"WeilJacquetShalikaLaw"): "Conclusion1",
    (7012,"LevelOfCongruence"): "each_unit_bound_statement", (7502,"WinPairs"): "winPairs",
    (7572,"Statement"): "TieEta", (7640,"Statement"): "PTShaAt", (7821,"Counts"): "GD",
    (11168,"Statement"): "SlopeIneq", (11168,"StatementPl"): "htMap",
    (11178,"Window"): "HasWindows", (11179,"WinPairs"): "winPairs", (12862,"Statement"): "BHyp",
}
# Short names the paper explicitly describes as files in a named directory.
SHORT_NAMES = [
    (4131,"CoarseMultiplicity","Loc4ResOfLine LiftSubstStart"),
    (9564,"Formalism/LocalRingCardinality","Params DataHost DataSpaces"),
    (9565,"Formalism/LocalRingCardinality","DataLevel DataForms DataCoeff DataKernels DataRows"),
    (9566,"Formalism/LocalRingCardinality","DataBu DataTies DataArith DataTheta DataJet"),
    (9567,"Formalism/LocalRingCardinality","DataParams₂ PosOfIsomEmb"),
    (9569,"Formalism/SharpRestriction","ElevenLe FamCore ParConsts"),
    (9570,"Formalism/SharpRestriction","GlobalTheoremInputs"),
    (9570,"CuspSpanNormBounds","DataS"), (9571,"GlobalSchurBounds","TieGlobal StandardLattice"),
    (9575,"LevelLetterCocycles","DataN"), (9575,"InertJacobiLevels","HostFam"),
    (9577,"LocalToGlobal/Divisibility","RecBridge Numbers"), (9578,"LocalToGlobal/Divisibility","Inputs"),
    (9578,"LocalToGlobal/Columns","TiedCH"), (11125,"LandauTheorems","ChTop ChCore"),
    (11127,"PrimitiveCosets","CoreGm"), (11128,"PrimitiveCosets","CoreAtH"),
    (11129,"GlobalSchurBounds","TieGlobal"),
]


def audit(tex, db, project):
    if hashlib.sha256(tex).hexdigest() != SHA:
        raise ValueError("Expected the pinned Version 2 TeX file")
    paths = defaultdict(list)
    for path, in db.execute("SELECT path FROM modules WHERE package='riemann-hypothesis' ORDER BY path"):
        paths[path.rsplit("/",1)[-1]].append(path)
    lines = tex.decode().splitlines()
    result = []
    for line_no,line in enumerate(lines,1):
        line = re.sub(r"\}\\linebreak\\path\{", "", line)
        for ref in re.findall(r"([\w./-]+\.lean)\b",line):
            suffix = ref.removeprefix("lean/")
            matches = [p for p in paths[suffix.rsplit("/",1)[-1]] if ("/"+p).endswith("/"+suffix)]
            n = len(matches)
            rule, witness = "literal path suffix", ""
            if n > 1:
                stem = ref.removesuffix(".lean")
                if name := WITNESSES.get((line_no,stem)):
                    witness = name
                    rule = "named declaration"
                    matches = [p for p in matches if db.execute(
                        "SELECT 1 FROM declarations d JOIN modules m ON m.id=d.module "
                        "WHERE m.path=? AND (d.name=? OR substr(d.name,-length(?)-1)='.'||?) LIMIT 1",
                        (p,name,name,name)).fetchone()]
                elif line_no == 9568:
                    rule, witness = "printed directory", "Formalism/LocalRingCardinality"
                    matches = [p for p in matches if p.endswith("/"+witness+"/"+ref)]
                elif line_no in (7016,11270):
                    rule = "named use in pinned source"
                    witness = "each_unit_bound_statement" if line_no == 7016 else "ComplementTwoFamily"
                    kept = []
                    for p in matches:
                        src = subprocess.check_output(["git","-C",project,"show",f"{PROOF}:{p}"],text=True).splitlines()
                        if any(witness in line for line in (src[33:34] if line_no==11270 else src)):
                            kept.append(p)
                    matches = kept
            result.append((line_no,ref,n,rule,witness,matches[0] if len(matches)==1 else ""))
    for line_no,folder,stems in SHORT_NAMES:
        for stem in stems.split():
            printed = "DataParams" if stem=="DataParams₂" else stem
            if r"\texttt{"+printed+"}" not in lines[line_no-1]:
                raise ValueError(f"Missing short name at {line_no}: {stem}")
            matches = [p for p in paths[stem+".lean"] if p.endswith("/"+folder+"/"+stem+".lean")]
            result.append((line_no,stem,len(matches),"short name and directory",folder,
                           matches[0] if len(matches)==1 else ""))
    return sorted(result)


if __name__ == "__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("tex",type=Path)
    cli.add_argument("database",type=Path)
    cli.add_argument("project",type=Path,help="Git checkout or bare copy containing the original Lean revision")
    args=cli.parse_args()
    with sqlite3.connect(args.database.resolve().as_uri()+"?mode=ro",uri=True) as db:
        rows=audit(args.tex.read_bytes(),db,args.project)
    out=csv.writer(sys.stdout,delimiter="\t",lineterminator="\n")
    out.writerow(["tex_line","reference","literal_candidates","evidence","witness","module"])
    out.writerows(rows)
