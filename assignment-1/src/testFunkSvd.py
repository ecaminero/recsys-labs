import time
import pyreclab


def main(factors=100):
    svd = pyreclab.SVD( dataset = 'dataset/u1.base',
                       dlmchar = b'\t',
                       header = False,
                       usercol = 0,
                       itemcol = 1,
                       ratingcol = 2 )

    print( '-> training model' )
    start = time.clock()
    svd.train(factors = factors, maxiter = 100, lr = 0.01, lamb = 0.1 )
    end = time.clock()
    print( 'training time: ' + str( end - start ) )

    print( '-> individual test' )
    pred = svd.predict( '457', '443' )
    print( 'user 457, item 443, prediction ' + str( pred ) )

    ranking = svd.recommend( '457', 5, includeRated = False )
    print( 'recommendation for user 457: ' + str( ranking ) )

    print( '-> prediction test' )
    start = time.clock()
    predlist, mae, rmse = svd.test( input_file = 'dataset/u1.test',
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
    recommendList = svd.testrec( input_file = 'dataset/u1.test',
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


    del svd

    time.sleep( 10 )
    return mae, rmse

if __name__ == '__main__':
    main()

