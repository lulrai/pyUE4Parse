from UE4Parse.BinaryReader import BinaryStream
from UE4Parse.Globals import FGame
from UE4Parse.Objects.EUEVersion import EUEVersion
from UE4Parse.Objects.Meshes.FRenderingObjectVersion import FRenderingObjectVersion


class FStaticMeshSection:
    MaterialIndex: int
    FirstIndex: int
    NumTriangles: int
    MinVertexIndex: int
    MaxVertexIndex: int
    EnableCollision: bool
    CastShadow: bool
    ForceOpaque: bool
    VisibleInRayTracing: bool

    def __init__(self, reader: BinaryStream):
        self.MaterialIndex = reader.readInt32()
        self.FirstIndex = reader.readInt32()
        self.NumTriangles = reader.readInt32()
        self.MinVertexIndex = reader.readInt32()
        self.MaxVertexIndex = reader.readInt32()
        self.EnableCollision = reader.readBool()
        self.CastShadow = reader.readBool()
        self.ForceOpaque = reader.readBool() if FRenderingObjectVersion().get() >= FRenderingObjectVersion.StaticMeshSectionForceOpaqueField else False
        self.VisibleInRayTracing = reader.readBool() if FGame.UEVersion.value >= EUEVersion.GAME_UE4_26.value else False

