import chess.src.pieces as pieces

ichiji_prefix = ":/Ichiji/resources/Ichiji/"
hidetchi_prefix = ":/Hidetchi/resources/hidetchi/"
prefix = hidetchi_prefix


def mapper():
    mpr = {
        "C_WP": {"resource": ":/Chess/resources/chess_48/Chess_plt48.png",
                 "piece": pieces.Pawn},
        "C_WR": {"resource": ":/Chess/resources/chess_48/Chess_rlt48.png",
                 "piece": pieces.Rook},
        "C_WN": {"resource": ":/Chess/resources/chess_48/Chess_nlt48.png",
                 "piece": pieces.Knight},
        "C_WB": {"resource": ":/Chess/resources/chess_48/Chess_blt48.png",
                 "piece": pieces.Bishop},
        "C_WQ": {"resource": ":/Chess/resources/chess_48/Chess_qlt48.png",
                 "piece": pieces.Queen},
        "C_WK": {"resource": ":/Chess/resources/chess_48/Chess_klt48.png",
                 "piece": pieces.King},
        "C_BP": {"resource": ":/Chess/resources/chess_48/Chess_pdt48.png",
                 "piece": pieces.Pawn},
        "C_BR": {"resource": ":/Chess/resources/chess_48/Chess_rdt48.png",
                 "piece": pieces.Rook},
        "C_BN": {"resource": ":/Chess/resources/chess_48/Chess_ndt48.png",
                 "piece": pieces.Knight},
        "C_BB": {"resource": ":/Chess/resources/chess_48/Chess_bdt48.png",
                 "piece": pieces.Bishop},
        "C_BQ": {"resource": ":/Chess/resources/chess_48/Chess_qdt48.png",
                 "piece": pieces.Queen},
        "C_BK": {"resource": ":/Chess/resources/chess_48/Chess_kdt48.png",
                 "piece": pieces.King},
        "C_WPR": {"resource": ":/Chess/resources/chess_48/Chess_rlt48.png",
                  "piece": pieces.Pawn},
        "C_WPN": {"resource": ":/Chess/resources/chess_48/Chess_nlt48.png",
                  "piece": pieces.Pawn},
        "C_WPB": {"resource": ":/Chess/resources/chess_48/Chess_blt48.png",
                  "piece": pieces.Pawn},
        "C_WPQ": {"resource": ":/Chess/resources/chess_48/Chess_qlt48.png",
                  "piece": pieces.Pawn},
        "C_BPR": {"resource": ":/Chess/resources/chess_48/Chess_rdt48.png",
                  "piece": pieces.Pawn},
        "C_BPN": {"resource": ":/Chess/resources/chess_48/Chess_ndt48.png",
                  "piece": pieces.Pawn},
        "C_BPB": {"resource": ":/Chess/resources/chess_48/Chess_bdt48.png",
                  "piece": pieces.Pawn},
        "C_BPQ": {"resource": ":/Chess/resources/chess_48/Chess_qdt48.png",
                  "piece": pieces.Pawn},
    }
    return mpr
