import time
import pyreclab

def main():
    slpone = pyreclab.SlopeOne( dataset = 'dataset/u1.base',
                               dlmchar = b'\t',
                               header = False,
                               usercol = 0,
                               itemcol = 1,
                               ratingcol = 2 )

    print( '-> training model' )
    start = time.clock()
    slpone.train()
    end = time.clock()
    print( 'training time: ' + str( end - start ) )

    print( '-> individual test' )
    pred = slpone.predict( '457', '443' )
    print( 'user 457, item 443, prediction ' + str( pred ) )

    ranking = slpone.recommend( '457', 5, includeRated = False )
    print( 'recommendation for user 457: ' + str( ranking ) )

    print( '-> prediction test' )
    start = time.clock()
    predlist, mae, rmse = slpone.test( input_file = 'dataset/u1.test',
                                      dlmchar = b'\t',
                                      header = False,
                                      usercol = 0,
                                      itemcol = 1,
                                      ratingcol = 2,
                                      output_file = 'predictions.csv' )
    end = time.clock()
    print( 'prediction time: ' + str( end - start ) )

    print( 'MAE: ' + str( mae ) )
    print( 'RMSE: ' + str( rmse ) )

    print( '-> recommendation test' )
    start = time.clock()
    recommendList = slpone.testrec( input_file = 'dataset/u1.test',
                                   dlmchar = b'\t',
                                   header = False,
                                   usercol = 0,
                                   itemcol = 1,
                                   ratingcol = 2,
                                   topn = 10,
                                   output_file = 'ranking.json',
                                   includeRated = False )
    end = time.clock()
    print( 'recommendation time: ' + str( end - start ) )

if __name__ == '__main__':
    main()
