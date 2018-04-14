import time
import pyreclab


def main(k=100):
    ibknn = pyreclab.ItemKnn( dataset = 'dataset/u1.base',
                             dlmchar = b'\t',
                             header = False,
                             usercol = 0,
                             itemcol = 1,
                             ratingcol = 2 )

    print( '-> training model' )
    start = time.clock()
    ibknn.train(k = k, similarity = 'pearson' )
    end = time.clock()
    print( 'training time: ' + str( end - start ) )

    print( '-> individual test' )
    pred = ibknn.predict( '457', '443' )
    print( 'user 457, item 443, prediction ' + str( pred ) )

    ranking = ibknn.recommend( '457', 5, includeRated = False )
    print( 'recommendation for user 457: ' + str( ranking ) )

    print( '-> prediction test' )
    start = time.clock()
    predlist, mae, rmse = ibknn.test( input_file = 'dataset/u1.test',
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
    recommendList = ibknn.testrec( input_file = 'dataset/u1.test',
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
    
    return mae, rmse


if __name__ == '__main__':
    main()