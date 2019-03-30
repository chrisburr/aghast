# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class InterpretedExternalBuffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInterpretedExternalBuffer(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InterpretedExternalBuffer()
        x.Init(buf, n + offset)
        return x

    # InterpretedExternalBuffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InterpretedExternalBuffer
    def Pointer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def Numbytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def ExternalSource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def Filters(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # InterpretedExternalBuffer
    def FiltersAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # InterpretedExternalBuffer
    def FiltersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # InterpretedExternalBuffer
    def PostfilterSlice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .Slice import Slice
            obj = Slice()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # InterpretedExternalBuffer
    def Dtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def Endianness(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def DimensionOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # InterpretedExternalBuffer
    def Location(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def InterpretedExternalBufferStart(builder): builder.StartObject(9)
def InterpretedExternalBufferAddPointer(builder, pointer): builder.PrependUint64Slot(0, pointer, 0)
def InterpretedExternalBufferAddNumbytes(builder, numbytes): builder.PrependUint64Slot(1, numbytes, 0)
def InterpretedExternalBufferAddExternalSource(builder, externalSource): builder.PrependUint32Slot(2, externalSource, 0)
def InterpretedExternalBufferAddFilters(builder, filters): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(filters), 0)
def InterpretedExternalBufferStartFiltersVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def InterpretedExternalBufferAddPostfilterSlice(builder, postfilterSlice): builder.PrependStructSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(postfilterSlice), 0)
def InterpretedExternalBufferAddDtype(builder, dtype): builder.PrependInt8Slot(5, dtype, 0)
def InterpretedExternalBufferAddEndianness(builder, endianness): builder.PrependInt8Slot(6, endianness, 0)
def InterpretedExternalBufferAddDimensionOrder(builder, dimensionOrder): builder.PrependInt8Slot(7, dimensionOrder, 0)
def InterpretedExternalBufferAddLocation(builder, location): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(location), 0)
def InterpretedExternalBufferEnd(builder): return builder.EndObject()