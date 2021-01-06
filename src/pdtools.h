#ifndef __PDTOOLS__
#define __PDTOOLS__

#include "PdBase.hpp"
#include "RtAudio.h"
#include "PdObject.h"
#include "externals/Externals.h"
#include <array>

int audioCallback(void *outputBuffer, void *inputBuffer, unsigned int nBufferFrames, double streamTime, RtAudioStreamStatus status, void *userData);
void initAudio(char *pdpatch);

#endif
