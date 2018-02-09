import sys
sys.path.append('./encoderSCMA')
sys.path.append('./decoderSCMA')
import encoderSCMA as encoder
import encoderConfig
import decoderSCMA
import config
import numpy as np


encoder.randomInputGenerator();
encoder.bin2codewords(encoderConfig.userInput);

config.resourceLayer = encoderConfig.finalInput[0];

decoderSCMA.iterativeMPA(7);
decoderSCMA.estimateSymbol();
difference = 0;
    #print(np.transpose(config.EstimatedSymbols));
    #print(np.transpose(encoderConfig.userSymbols));
for ele in np.absolute(config.EstimatedSymbols-encoderConfig.userSymbols):
    difference += ele;
print("Symbol_error",difference);
